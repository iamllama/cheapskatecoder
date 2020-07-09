import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopNineBlogsComponent } from './top-nine-blogs.component';

describe('TopNineBlogsComponent', () => {
  let component: TopNineBlogsComponent;
  let fixture: ComponentFixture<TopNineBlogsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopNineBlogsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopNineBlogsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
