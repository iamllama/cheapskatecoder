import { Component, OnInit } from '@angular/core';
import {TopNineBlogsService} from './../../../../services/includes/top-nine-blogs.service';
import Blog from './../../../../models/blog.models';

@Component({
  selector: 'app-top-nine-blogs',
  templateUrl: './top-nine-blogs.component.html',
  styleUrls: ['./top-nine-blogs.component.css']
})

export class TopNineBlogsComponent implements OnInit {

  constructor(private top9blogservice: TopNineBlogsService) { }
  topNineBlogs: Blog[] = new Array<Blog>();

  ngOnInit(): void {
    this.top9blogservice.getTopNineBlogs().subscribe(response => {
      this.topNineBlogs = response;
    });
  }

}
