import { Component, OnInit } from '@angular/core';
import {TopNineBlogsService} from './../../../../services/includes/top-nine-blogs.service';

@Component({
  selector: 'app-top-nine-blogs',
  templateUrl: './top-nine-blogs.component.html',
  styleUrls: ['./top-nine-blogs.component.css']
})

export class TopNineBlogsComponent implements OnInit {

  constructor(private top9blogservice: TopNineBlogsService) { }
  topNineBlogs;

  ngOnInit(): void {
    this.top9blogservice.getTopNineBlogs().subscribe(response => this.topNineBlogs = response);
    console.log(this.topNineBlogs);
  }

}
