import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { RoleGuard } from './guards/role.guard';

//Componentes
import { CreateSurveyComponent } from './create-survey/create-survey.component'
import { CreateSectionComponent } from './create-section/create-section.component'
import { CreateQuestionComponent } from './create-question/create-question.component';
import { LoginComponent } from './login/login.component';
import { LayoutComponent } from './layout/layout.component';
import { CreateFlujoComponent } from './create-flujo/create-flujo.component';
import { UserInitialPageComponent } from './user-initial-page/user-initial-page.component';
import { CreateUserComponent } from './create-user/create-user.component';
import { ShowUserInfoComponent } from './show-user-info/show-user-info.component';
import { ModifyFlujoComponent } from './modify-flujo/modify-flujo.component';
import { ModifyUserComponent } from './modify-user/modify-user.component';
import { PruebasComponent } from './pruebas/pruebas.component';
import { ModifySurveyComponent } from './modify-survey/modify-survey.component';
import { AdminInitialPageComponent } from './admin-initial-page/admin-initial-page.component';
import { AsignarFlujoComponent } from './asignar-flujo/asignar-flujo.component';

const routes: Routes = [
  {
    path: '', canActivate:[AuthGuard], component: LayoutComponent, children: [
      {
        path: 'create_survey', component: CreateSurveyComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'create_section', component: CreateSectionComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'create_question', component: CreateQuestionComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'create_flujo', component: CreateFlujoComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'create_user', component: CreateUserComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'user_info', component: ShowUserInfoComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'modify_flujo', component: ModifyFlujoComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'modify_user', component: ModifyUserComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }, {
        path: 'modify_survey', component: ModifySurveyComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      },{ 
        path: 'admin_initial_page', component: AdminInitialPageComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      },{ 
        path: 'user_initial_page', component: UserInitialPageComponent
      },{ 
        path: 'asignar_flujo', component: AsignarFlujoComponent, canActivate:[RoleGuard], data:{requiredRoles: ['admin', 'profesional']}
      }
    ]
  },{ 
    path: 'login_page', component: LoginComponent 
  },{ 
    path: 'playground', component: PruebasComponent
  }
  //{ path: 'create_survey', component: CreateSurveyComponent },
  //{ path: 'create_section', component: CreateSectionComponent },
  //{ path: 'create_question', component: CreateQuestionComponent },
  //{ path: 'login_page', component: LoginComponent },
  //{ path: '', redirectTo: '/login_page', pathMatch: 'full' }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
