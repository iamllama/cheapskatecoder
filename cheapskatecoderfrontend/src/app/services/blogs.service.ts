import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import Blog from '../models/blog.models';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class BlogsService {
  constructor(private http: HttpClient) {}

  getAllBlogs(): Observable<any> {
    return this.http.get<any>(environment.API_PREFIX + 'blog');
  }
}
