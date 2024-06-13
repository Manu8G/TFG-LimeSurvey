import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/usuario/usuario.module';
import { Flujo } from '../../models/flujo/flujo.module';
import { PreguntaMultiple } from '../../models/pregunta-multiple/pregunta-multiple.module';
import { Paciente } from '../../models/paciente/paciente.module';

@Injectable({
  providedIn: 'root'
})
export class FlujoService {
  private createFlujoURL = 'http://localhost:8000/admin/create_flujo/';
  private listFlujosURL = 'http://localhost:8000/admin/listar_flujos/';
  private asignarFlujoURL = 'http://localhost:8000/admin/asignar_flujos/';
  
  constructor(private http: HttpClient) { }

  createFlujo(data: Flujo): Observable<any> {
    console.log("asdf asdfwwwd", data);
    return this.http.post<any>(this.createFlujoURL, data);
  }

  listFlujos(): Observable<any> {
    return this.http.get<any>(this.listFlujosURL);
  }

  asignarFlujo(data: Flujo): Observable<any> {
    return this.http.post<any>(this.asignarFlujoURL, data);
  }

}
