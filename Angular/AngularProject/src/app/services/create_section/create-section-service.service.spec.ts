import { TestBed } from '@angular/core/testing';

import { CreateSectionServiceService } from './create-section-service.service';

describe('CreateSectionServiceService', () => {
  let service: CreateSectionServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreateSectionServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
