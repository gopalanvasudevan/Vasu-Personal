import { Component, EventEmitter, Output, OnInit } from '@angular/core';
//import { Post } from '../post.model';
import { NgForm } from '@angular/forms';
import { PostsService } from '../posts.service';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Post } from '../post.model';

@Component({
  selector: 'app-post-create',
  templateUrl: './post-create.component.html',
  styleUrls: ['./post-create.component.css']
})

export class PostCreateComponent implements OnInit{
  enteredTitle = '';
  enteredContent = '';
  private mode = 'create';
  private postId:string;
  isLoading = false;
  post: Post;
  //paramMap: any;

  //create an event, and tell Angular to listen for it
  //Output decorator
  //Emitter will send data of type Post
  //@Output() postCreated = new EventEmitter<Post>();

  //ActivatedRoute holds the dynamic information
  constructor(public postsService: PostsService, public route: ActivatedRoute) { }

  ngOnInit(){

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
      } else {
        this.mode = 'create';
        this.postId=null;
      }
    });
  }

  onSavePost(form: NgForm) {
    if (form.invalid) {
      return;
    }

    this.isLoading = true;
    if (this.mode === 'create') {
      this.postsService.addPost(form.value.title, form.value.content);
    } else {
      this.postsService.updatePost(this.postId, form.value.title, form.value.content);
    }

    //Clear form contents
    form.resetForm();

  }
}
