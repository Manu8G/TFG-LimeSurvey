import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/usuario/usuario.module';
import { Pregunta } from '../../models/pregunta/pregunta.module';
import { PreguntaMultiple } from '../../models/pregunta-multiple/pregunta-multiple.module';
import { Paciente } from '../../models/paciente/paciente.module';

@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private createSurveyURL = 'http://localhost:8000/admin/create_survey/';
  private createSurveyInDBURL = 'http://localhost:8000/admin/create_survey_in_db/';
  private createSectionURL = 'http://localhost:8000/admin/create_section/';
  private createTextQuestionURL = 'http://localhost:8000/admin/create_text_question/';
  private createMultipleQuestionURL = 'http://localhost:8000/admin/create_multiple_question/';
  private listIDSurveyURL = 'http://localhost:8000/admin/get_survey_id/';
  private listIDSectionURL = 'http://localhost:8000/admin/get_section_id/';
  private createUserURL = 'http://localhost:8000/admin/create_user/';
  private createPatientURL = 'http://localhost:8000/admin/create_patient/';
  private listUsersForAdminURL = 'http://localhost:8000/admin/list_users_for_admin/';
  private listUsersForProfesionalURL = 'http://localhost:8000/admin/list_users_for_profesional/';
  private listFlujoURL = 'http://localhost:8000/admin/list_flujo/';

  constructor(private http: HttpClient) { }

  createSurvey(data: any): Observable<any> {
    return this.http.post<any>(this.createSurveyURL, data);
  }

  createSurveyInDB(data: any): Observable<any> {
    return this.http.post<any>(this.createSurveyInDBURL, data);
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

  listIDSection(id_survey: string): Observable<any> {
    const estructura = {id: id_survey};
    return this.http.post<any>(this.listIDSectionURL, estructura);
  }

  createUser(data: Usuario): Observable<any> {
    return this.http.post<any>(this.createUserURL, data);
  }

  createPatientUser(data: Paciente): Observable<any> {
    return this.http.post<any>(this.createPatientURL, data);
  }

  listAdminUsers(): Observable<any> {
    return this.http.get<any>(this.listUsersForAdminURL);
  }
  
  listProfesionalUsers(): Observable<any> {
    return this.http.get<any>(this.listUsersForProfesionalURL);
  }

  listFlujo(): Observable<any> {
    return this.http.get<any>(this.listFlujoURL);
  }


}
