import { Component, OnInit } from '@angular/core';
import { SpecificBlogService } from './../../../../services/includes/specific-blog.service';
import Blog from './../../../../models/blog.models';

@Component({
  selector: 'app-specific-blog',
  templateUrl: './specific-blog.component.html',
  styleUrls: ['./specific-blog.component.css'],
})

export class SpecificBlogComponent implements OnInit {
  constructor(private specificBlogService: SpecificBlogService) {}
  specificBlog: Blog;

  ngOnInit(): void {
    const slug: string = location.pathname.split('/')[2];
    this.specificBlogService.getSpecificBlog(slug).subscribe((response) => {
      this.specificBlog = response;
    });
    window.scrollTo(0, 0);
  }
}
