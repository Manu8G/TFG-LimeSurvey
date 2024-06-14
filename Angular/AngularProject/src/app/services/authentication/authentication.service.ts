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
  //public idUsuario: number = 0;
  private idUsuarioSubject: BehaviorSubject<number | null> = new BehaviorSubject<number | null>(null);
  public idUsuario$: Observable<number | null> = this.idUsuarioSubject.asObservable();
  // public currentUser: Observable<Usuario | null>;

  private createTokenURL = 'http://localhost:8000/admin/token/';
  private getUserID = 'http://localhost:8000/admin/get_user_id/';


  constructor(private http: HttpClient, private router: Router) { 
    // this.currentUserSubject =  new BehaviorSubject<Usuario>(JSON.parse(localStorage.getItem('currentUser')));
    // this.currentUser = this.currentUserSubject.asObservable();
  }

  createToken(data: Partial<Usuario>): void { //CAMBIAR NOMBRE - SE HA CAMBIADO DE OBSERVABLE<ANY> A ANY
    this.http.post<any>(this.createTokenURL, data).subscribe({
      next: (response: any)=>{
        console.log(" es estas");
        console.log(response);
        const userCurrent: Partial<Usuario> = {
          name: data.name,
          password: '',
          role: response.role,
          accessToken: response.access_token, 
          id: response.id   
        };
        console.log("este es el id q ricibimos: ",response.id);
        // this.getUserId(userCurrent).subscribe({
        //   next: (id) => {
        //     this.idUsuarioSubject.next(id);  // Asegúrate de que 'id' sea un número
        //     console.log('waka waka waka234: ',this.idUsuarioSubject.value);
        //   },
        //   error: (err) => {
        //     console.error('Error fetching user ID:', err);
        //   }
        // });
        
        localStorage.setItem('token', JSON.stringify(response.access_token));
        localStorage.setItem('currentUser', JSON.stringify(userCurrent));
        this.userLogged.next(userCurrent);
        this.isAuthenticated.next(true); //HACER UN IF ROL QUE VAYA A UN SITIO U OTRO
        if(userCurrent.role == 'paciente'){
          this.router.navigate(['/user_initial_page']);
        }else{
          this.router.navigate(['/admin_initial_page']);
        }
        
      },
      error:()=>{
        this.isAuthenticated.next(false);
        // localStorage.clear();
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
    console.log("mensaje34: ",JSON.parse(localStorage.getItem('currentUser') as unknown as string))
    console.log("mensaje35: ",(JSON.parse(localStorage.getItem('currentUser') as unknown as string)).id)
    return (JSON.parse(localStorage.getItem('currentUser') as unknown as string)).id
  }


}
