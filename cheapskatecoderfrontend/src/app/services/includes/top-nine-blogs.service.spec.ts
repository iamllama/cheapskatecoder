import { TestBed } from '@angular/core/testing';

import { TopNineBlogsService } from './top-nine-blogs.service';

describe('TopNineBlogsService', () => {
  let service: TopNineBlogsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TopNineBlogsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
