import { Component, Input, OnInit, OnDestroy } from '@angular/core';
import { Post } from '../post.model';
import { PostsService } from '../posts.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls:['./post-list.component.css']
})
export class PostListComponent implements OnInit, OnDestroy {
  //posts = [
    // {title:'First Post', content:'Content of first post'},
    // {title:'Second Post', content:'Content of second post'},
    // {title:'Third Post', content:'Content of third post'}
  //]
  posts: Post[] = [];
  private postsSub: Subscription;
  isLoading = false;

  constructor(public postsService: PostsService){}
    //Angular will automatically execute this function, when this contructor is created
    ngOnInit(){
      this.isLoading = true;
      this.postsService.getPosts();
      //subscribe to the observarable listener
      this.postsSub = this.postsService.getPostUpdateListener()
        .subscribe((posts: Post[]) => {
          this.isLoading = false;
          this.posts=posts;
        });
    }

    onDelete(postId: string){
      alert(postId);
      this.postsService.deletePost(postId);

    }

    ngOnDestroy(){
      this.postsSub.unsubscribe;
    }

}
