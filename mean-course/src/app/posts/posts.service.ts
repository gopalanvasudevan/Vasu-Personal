import { Post } from './post.model';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Router } from '@angular/router';

//RxJS (Reactive Extensions for JavaScript) is a library for reactive programming using
//observables that makes it easier to compose asynchronous or callback-based code

//makes single instance of this class available for access across the modules
@Injectable({providedIn: 'root'})
export class PostsService {
  private posts: Post[] = [];
  private postsUpdated = new Subject<Post[]>();

  //instantiate object for accessing http values
  constructor(private http: HttpClient, private router:Router) {}

  getPosts(){
    //alert('inside getPosts');
    //returning this.posts will still refer the original object,
    //hence return a copy of the array by using below syntax, and make it immutable
    //return [...this.posts];
    //return this.posts;
    this.http
    .get<{message: string, posts: any}>('http://localhost:3000/api/posts')
    //since front-end expects it as id, convert _id being received from DB
    //to id using map function
    .pipe(map((postData) => {
      return postData.posts.map(post => {
        return {
          title : post.title,
          content : post.content,
          id: post._id
        }
      });
    }))
    .subscribe((transformedPosts) => {
      this.posts = transformedPosts;
      //pass copy of postsUpdated as output
      this.postsUpdated.next([...this.posts]);
    });
    console.log(this.posts);
  }

  public getPostUpdateListener(){
    return this.postsUpdated.asObservable();
  }

  addPost (title: string, content: string){
    const post: Post = {id:null, title: title, content: content};

    this.http.post<{message: string, postId: string}>('http://localhost:3000/api/posts',post)
    .subscribe((responseData) => {
      console.log("Response Message is :",responseData.message);

      //Assign back the id of the post from DB to the id of local object, else without refresh
      //if we add and then immediately delete, id getting passed would be null
      const id = responseData.postId;
      post.id = id;


      this.posts.push(post);
      //pass copy of postsUpdated as output
      this.postsUpdated.next([...this.posts]);
      //Route the user to the messages listing page
      this.router.navigate(["/"]);
    });
  }

  getPost(id: string){
    //return copy of the post object by matching with the id
    return {...this.posts.find(p => p.id === id)};
  }

  updatePost(id: string, title: string, content: string){
    const post:Post= { id:id, title:title, content:content} ;
    this.http.put("http://localhost:3000/api/posts/"+ id, post)
    .subscribe(response => console.log(response));
    this.router.navigate(["/"]);
  }

  deletePost(postId: string){
    this.http.delete("http://localhost:3000/api/posts/"+ postId)
    .subscribe(() => {
      console.log('Deleted !');
      //In UI, posts should get auto-refreshed i.e. should not contain the item that has got deleted now.
      //So, filter for the items to be retained where postId is not equal to the one being deleted.
      //Without this code snippet, user would need to refresh the screen, to notice the item having got deleted
      const updatedPosts = this.posts.filter(post => post.id !== postId);
      this.posts = updatedPosts;
      this.postsUpdated.next([...this.posts]);
    });
  }

}
