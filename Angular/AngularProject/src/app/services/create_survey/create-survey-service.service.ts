import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/usuario/usuario.module';
import { Pregunta } from '../../models/pregunta/pregunta.module';
import { PreguntaMultiple } from '../../models/pregunta-multiple/pregunta-multiple.module';


@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private createSurveyURL = 'http://localhost:8000/admin/create_survey/';
  private createSectionURL = 'http://localhost:8000/admin/create_section/';
  private createTextQuestionURL = 'http://localhost:8000/admin/create_text_question/';
  private createMultipleQuestionURL = 'http://localhost:8000/admin/create_multiple_question/';
  private listIDSurveyURL = 'http://localhost:8000/admin/get_survey_id/';
  private listIDSectionURL = 'http://localhost:8000/admin/get_section_id/';
  private createUserURL = 'http://localhost:8000/admin/create_user/';
  

  constructor(private http: HttpClient) { }

  createSurvey(data: any): Observable<any> {
    return this.http.post<any>(this.createSurveyURL, data);
  }

  createSection(data: any): Observable<any> {
    return this.http.post<any>(this.createSectionURL, data);
  }

  createTextQuestion(data: Pregunta): Observable<any> {
    return this.http.post<any>(this.createTextQuestionURL, data);
  }

  createMultipleQuestion(data: PreguntaMultiple): Observable<any> {
    return this.http.post<any>(this.createMultipleQuestionURL, data);
  }

  listIDSurvey(): Observable<any> {
    return this.http.get<any>(this.listIDSurveyURL);
  }
// console.log("Tipo id survey vairbale tiplo");
    // console.log(typeof id_survey);
    // console.log(id_survey);
    // console.log(id_survey[0]);
  listIDSection(id_survey: string): Observable<any> {
    const estructura = {id: id_survey};
    return this.http.post<any>(this.listIDSectionURL, estructura);
  }

  createUser(data: Usuario): Observable<any> {
    return this.http.post<any>(this.createUserURL, data);
  }

}
