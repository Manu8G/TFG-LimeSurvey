import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Flujo } from '../../models/flujo/flujo.module';
import { Caso } from '../../models/caso/caso.module';
import { Id } from '../../models/id/id.module';

@Injectable({
  providedIn: 'root'
})
export class FlujoService {
  private createFlujoURL = 'http://localhost:8000/admin/create_flujo/';
  private listFlujosURL = 'http://localhost:8000/admin/listar_flujos/';
  private asignarFlujoURL = 'http://localhost:8000/admin/asignar_flujo/';
  private getCasoURL = 'http://localhost:8000/admin/get_caso/';
  
  constructor(private http: HttpClient) { }

  createFlujo(data: Flujo): Observable<any> {
    return this.http.post<any>(this.createFlujoURL, data);
  }

  listFlujos(): Observable<any> {
    return this.http.get<any>(this.listFlujosURL);
  }

  asignarFlujo(data: Caso): Observable<any> {
    return this.http.post<any>(this.asignarFlujoURL, data);
  }

  getCaso(data: Id): Observable<any> {
    return this.http.post<any>(this.getCasoURL, data);
  }

}
