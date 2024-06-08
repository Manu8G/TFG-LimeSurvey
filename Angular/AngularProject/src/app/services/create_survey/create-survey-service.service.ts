import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/usuario/usuario.module';

@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private createSurveyURL = 'http://localhost:8000/admin/create_survey/';
  private createSectionURL = 'http://localhost:8000/admin/create_section/';
  private createQuestionURL = 'http://localhost:8000/create_question/';
  private listIDSurveyURL = 'http://localhost:8000/admin/get_survey_id/';
  private listIDSectionURL = 'http://localhost:8000/list_sections/';
  private createUserURL = 'http://localhost:8000/admin/create_user/';
  

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

  listIDSurvey(): Observable<any> {
    return this.http.get<any>(this.listIDSurveyURL);
  }

  listIDSection(data: any): Observable<any> {
    return this.http.post<any>(this.listIDSectionURL, data);
  }

  createUser(data: Usuario): Observable<any> {
    return this.http.post<any>(this.createUserURL, data);
  }

}
