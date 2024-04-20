import { TestBed } from '@angular/core/testing';

import { CreateSurveyServiceService } from './create-survey-service.service';

describe('CreateSurveyServiceService', () => {
  let service: CreateSurveyServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreateSurveyServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
