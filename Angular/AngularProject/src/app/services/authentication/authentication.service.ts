import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Usuario } from '../../models/usuario/usuario.module';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  // private currentUserSubject: BehaviorSubject<Usuario | null>;
  // if(localStorage){

  // }else{

  // }
  public userLogged: BehaviorSubject<Partial<Usuario> | null> = new BehaviorSubject(JSON.parse(localStorage.getItem('currentUser') || '{}'));
  public isAuthenticated: BehaviorSubject<boolean> = new BehaviorSubject(localStorage.getItem('token') !== null);
  // public currentUser: Observable<Usuario | null>;

  private createTokenURL = 'http://localhost:8000/admin/token/';

  constructor(private http: HttpClient, private router: Router) { 
    // this.currentUserSubject =  new BehaviorSubject<Usuario>(JSON.parse(localStorage.getItem('currentUser')));
    // this.currentUser = this.currentUserSubject.asObservable();
  }

  createToken(data: Partial<Usuario>): void { //CAMBIAR NOMBRE - SE HA CAMBIADO DE OBSERVABLE<ANY> A ANY
    this.http.post<any>(this.createTokenURL, data).subscribe({
      next: (response: any)=>{
        // console.log(" es estas");
        // console.log(response);
        const userCurrent: Partial<Usuario> = {
          name: data.name,
          password: '',
          role: response.role,
          accessToken: response.access_token,    
        };
        localStorage.setItem('token', JSON.stringify(response.access_token));
        localStorage.setItem('currentUser', JSON.stringify(userCurrent));
        this.userLogged.next(userCurrent);
        this.isAuthenticated.next(true); //HACER UN IF ROL QUE VAYA A UN SITIO U OTRO
        this.router.navigate(['/']);
      },
      error:()=>{
        this.isAuthenticated.next(false);
        // localStorage.clear();
      }
    });

  }

  logout(){
    localStorage.removeItem('currentUser');
    this.userLogged.next(null);
    this.isAuthenticated.next(false);
    this.router.navigate(['/login_page']); //COMPROBAR SI ESTO ES CORRECTO
  }

  hasRole(roles: string[]): boolean{
    for(let role of roles){
      if(JSON.parse(localStorage.getItem('currentUser') as unknown as string) && JSON.parse(localStorage.getItem('currentUser')as unknown as string).role === role){
        return true;
      }
    }
    return false;
  }

}
