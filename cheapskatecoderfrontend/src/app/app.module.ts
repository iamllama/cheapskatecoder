import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { TopNineBlogsComponent } from './components/home/includes/top-nine-blogs/top-nine-blogs.component';
import { PrivacyPolicyComponent } from './components/privacy-policy/privacy-policy.component';
import { TermsAndConditionsComponent } from './components/terms-and-conditions/terms-and-conditions.component';
import { BlogComponent } from './components/blog/blog.component';
import { SpecificBlogComponent } from './components/blog/includes/specific-blog/specific-blog.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TopNineBlogsComponent,
    PrivacyPolicyComponent,
    TermsAndConditionsComponent,
    BlogComponent,
    SpecificBlogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
