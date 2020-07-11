import { Component, OnInit } from '@angular/core';
import { BlogsService } from './../.././services/blogs.service';
import Blog from './../../models/blog.models';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css'],
})
export class BlogComponent implements OnInit {
  constructor(private allBlogService: BlogsService) {}

  allBlogs: any;

  ngOnInit(): void {
    this.allBlogService.getAllBlogs().subscribe((response) => {
      this.allBlogs = response;
      console.log(this.allBlogs.results[0].slug);
    });
  }
}
