import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import Blog from './../../models/blog.models';
import {environment} from './../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TopNineBlogsService {

  constructor(private http: HttpClient) { }

  getTopNineBlogs(): Observable<Blog[]> {
    return this.http.get<any>(environment.API_PREFIX + 'top-9-blogs');
  }
}
