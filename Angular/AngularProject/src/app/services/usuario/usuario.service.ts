import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Usuario } from '../../models/usuario/usuario.module';
import { Paciente } from '../../models/paciente/paciente.module';
import { Correo } from '../../models/correo/correo.module';
import { Id } from '../../models/id/id.module';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  private createUserURL = 'http://localhost:8000/admin/create_user';
  private createPatientURL = 'http://localhost:8000/admin/create_patient';
  private listUsersForAdminURL = 'http://localhost:8000/admin/list_users_for_admin';
  private listUsersForProfesionalURL = 'http://localhost:8000/admin/list_users_for_profesional';
  private mandarCorreoURL = 'http://localhost:8000/admin/mandar_correo';
  private getUserInfoURL = 'http://localhost:8000/admin/get_user_info';

  constructor(private http: HttpClient) { }

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

  mandarCorreo(data: Correo): Observable<any> {
    return this.http.post<any>(this.mandarCorreoURL, data);
  } 

  getUserInfo(data: Id): Observable<any> {
    return this.http.post<any>(this.getUserInfoURL, data);
  }

}
