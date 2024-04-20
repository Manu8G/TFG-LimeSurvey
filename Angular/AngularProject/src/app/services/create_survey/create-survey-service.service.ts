import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CreateSurveyServiceService {

  private apiUrl = 'http://localhost:8000/create_survey/';

  constructor(private http: HttpClient) { }

  modifyData(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

}
