import { Component, EventEmitter, Output, OnInit } from '@angular/core';
//import { Post } from '../post.model';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { PostsService } from '../posts.service';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Post } from '../post.model';
import { mimeType } from './mime-type.validator';

@Component({
  selector: 'app-post-create',
  templateUrl: './post-create.component.html',
  styleUrls: ['./post-create.component.css']
})

export class PostCreateComponent implements OnInit{
  enteredTitle = '';
  enteredContent = '';
  private mode = 'create';
  private postId: string;
  isLoading = false;
  imagePreview: string;
  post: Post;
  form: FormGroup;
  //paramMap: any;

  //create an event, and tell Angular to listen for it
  //Output decorator
  //Emitter will send data of type Post
  //@Output() postCreated = new EventEmitter<Post>();

  //ActivatedRoute holds the dynamic information
  constructor(public postsService: PostsService, public route: ActivatedRoute) { }

  ngOnInit(){

    //For moving away from template driven model to Reactive model, create the form object here, and access this
    //object in html file
    this.form = new FormGroup({
      'title': new FormControl(null, 
        {validators:[Validators.required, Validators.minLength(1)]}),
      'content': new FormControl(null, {validators:[Validators.required]}),
      'image': new FormControl(null, {validators:[Validators.required], asyncValidators:[mimeType]})
    });
    //as seen above, call the mimeType function asynchronously

    //listen to this observable
    //since this PostCreateComponent will be used for both add and edit of posts, we need to differentiate
    //between the modes
    this.route.paramMap.subscribe((paramMap: ParamMap) => {
      if (paramMap.has('postId')){
        this.mode = 'edit';
        this.postId = paramMap.get('postId');
        //Use this flag for showing the spinner icon
        this.isLoading = true;
        console.log(this.isLoading);
        this.post=this.postsService.getPost(this.postId);
        this.isLoading = false;
        console.log(this.isLoading);
        this.form.setValue({
          'title':this.post.title,
          'content':this.post.content});
      } else {
        this.mode = 'create';
        this.postId=null;
      }
    });
  }

  onImagePicked(event: Event){
    //alert('inside onImagePicked');
    const file = (event.target as HTMLInputElement).files[0];
    //associate the selected file to the image object
    this.form.patchValue({image: file});
    this.form.get('image').updateValueAndValidity();
    console.log(file);
    console.log(this.form);
    const reader = new FileReader();
    reader.onload = () => {
      this.imagePreview = reader.result as string;
    }
    reader.readAsDataURL(file);
  }

  onSavePost() {
    if (this.form.invalid) {
      return;
    }

    this.isLoading = true;
    if (this.mode === 'create') {
      this.postsService.addPost(this.form.value.title, this.form.value.content);
    } else {
      this.postsService.updatePost(this.postId, this.form.value.title, this.form.value.content);
    }

    //Clear form contents
    this.form.reset();

  }
}
