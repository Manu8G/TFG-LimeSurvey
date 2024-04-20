import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CreateSectionServiceService {

  private apiUrl = 'http://localhost:8000/create_section/';

  constructor(private http: HttpClient) { }

  modifyData(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

}
