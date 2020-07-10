import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import Blog from './../../models/blog.models';

@Injectable({
  providedIn: 'root',
})
export class SpecificBlogService {
  constructor(private http: HttpClient) {}

  getSpecificBlog(slug): Observable<Blog> {
    return this.http.get<any>(environment.API_PREFIX + 'blog/' + slug);
  }
}
