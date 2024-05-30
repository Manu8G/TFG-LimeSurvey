import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private createSurveyURL = 'http://localhost:8000/create_survey/';
  private createSectionURL = 'http://localhost:8000/create_section/';
  private createQuestionURL = 'http://localhost:8000/create_question/'
  private listIDSurveyURL = 'http://localhost:8000/get_survey_id/'
  private listIDSectionURL = 'http://localhost:8000/list_sections/'

  constructor(private http: HttpClient) { }

  createSurvey(data: any): Observable<any> {
    return this.http.post<any>(this.createSurveyURL, data);
  }

  createSection(data: any): Observable<any> {
    return this.http.post<any>(this.createSectionURL, data);
  }

  createQuestion(data: any): Observable<any> {
    return this.http.post<any>(this.createQuestionURL, data);
  }

  listIDSurvey(data: any): Observable<any> {
    return this.http.post<any>(this.listIDSurveyURL, data);
  }

  listIDSection(data: any): Observable<any> {
    return this.http.post<any>(this.listIDSectionURL, data);
  }

}
