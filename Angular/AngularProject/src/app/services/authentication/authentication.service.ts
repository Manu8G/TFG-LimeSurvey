import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { FullUsuario } from '../../models/full-user/full-user.module';
import { Usuario } from '../../models/usuario/usuario.module';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  public userLogged: BehaviorSubject<Partial<Usuario> | null> = new BehaviorSubject(JSON.parse(localStorage.getItem('currentUser') || '{}'));
  public isAuthenticated: BehaviorSubject<boolean> = new BehaviorSubject(localStorage.getItem('token') !== null);
  private idUsuarioSubject: BehaviorSubject<number | null> = new BehaviorSubject<number | null>(null);
  public idUsuario$: Observable<number | null> = this.idUsuarioSubject.asObservable();

  private createTokenURL = 'http://localhost:8000/admin/token/';


  constructor(private http: HttpClient, private router: Router) {
  }

  createToken(data: Partial<Usuario>): void {
    this.http.post<any>(this.createTokenURL, data).subscribe({
      next: (response: any)=>{
        const userCurrent: FullUsuario = {
          name: String(data.name),
          password: '',
          role: response.role,
          accessToken: response.access_token, 
          id: response.id   
        };
        
        localStorage.setItem('token', JSON.stringify(response.access_token));
        localStorage.setItem('currentUser', JSON.stringify(userCurrent));
        this.userLogged.next(userCurrent);
        this.isAuthenticated.next(true); 
        if(userCurrent.role == 'paciente'){
          this.router.navigate(['/user_initial_page']);
        }else{
          this.router.navigate(['/admin_initial_page']);
        }
        
      },
      error:()=>{
        this.isAuthenticated.next(false);
      }
    });
    
  }

  logout(){
    localStorage.removeItem('currentUser');
    localStorage.removeItem('token');
    this.userLogged.next(null);
    this.isAuthenticated.next(false);
    this.router.navigate(['/login_page']);
  }

  hasRole(roles: string[]): boolean{
    for(let role of roles){
      if(JSON.parse(localStorage.getItem('currentUser') as unknown as string) && JSON.parse(localStorage.getItem('currentUser')as unknown as string).role === role){
        return true;
      }
    }
    return false;
  }

  getRole(): string {
    return (JSON.parse(localStorage.getItem('currentUser') as unknown as string)).role
  }

  getUserId(): string{
    return (JSON.parse(localStorage.getItem('currentUser') as unknown as string)).id
  }


}
