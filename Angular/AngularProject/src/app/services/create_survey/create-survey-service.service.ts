import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Pregunta } from '../../models/pregunta/pregunta.module';
import { PreguntaMultiple } from '../../models/pregunta-multiple/pregunta-multiple.module';
import { Id } from '../../models/id/id.module';
import { EncuestaDB } from '../../models/encuesta-bd/encuesta-bd.module';
import { Encuesta } from '../../models/encuesta/encuesta.module';


@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private createSurveyURL = 'http://localhost:8000/admin/create_survey';
  private createSurveyInDBURL = 'http://localhost:8000/admin/create_survey_in_db';
  private createSectionURL = 'http://localhost:8000/admin/create_section';
  private createTextQuestionURL = 'http://localhost:8000/admin/create_text_question';
  private createMultipleQuestionURL = 'http://localhost:8000/admin/create_multiple_question';
  private listIDSurveyURL = 'http://localhost:8000/admin/get_survey_id';
  private listIDSectionURL = 'http://localhost:8000/admin/get_section_id';
  private eliminarEncuestaURL = 'http://localhost:8000/admin/eliminar_encuesta';
  

  constructor(private http: HttpClient) { }

  createSurvey(data: Encuesta): Observable<any> {
    return this.http.post<any>(this.createSurveyURL, data);
  }

  createSurveyInDB(data: EncuestaDB): Observable<any> {
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

  listIDSection(id: Id): Observable<any> {
    return this.http.post<any>(this.listIDSectionURL, id);
  }

  eliminarEncuesta(data: Id): Observable<any> {
    console.log('vmaos a lallamosdm',data);
    console.log('urld',this.eliminarEncuestaURL);
    
    return this.http.post<any>(this.eliminarEncuestaURL, data);
  }

}
