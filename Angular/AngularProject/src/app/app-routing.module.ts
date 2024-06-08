import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';

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

const routes: Routes = [
  {
    path: '', canActivate:[AuthGuard], component: LayoutComponent, children: [
      {
        path: 'create_survey', component: CreateSurveyComponent
      }, {
        path: 'create_section', component: CreateSectionComponent
      }, {
        path: 'create_question', component: CreateQuestionComponent
      }, {
        path: 'create_flujo', component: CreateFlujoComponent
      }, {
        path: 'create_user', component: CreateUserComponent
      }, {
        path: 'user_info', component: ShowUserInfoComponent
      }, {
        path: 'modify_flujo', component: ModifyFlujoComponent
      }, {
        path: 'modify_user', component: ModifyUserComponent
      }, {
        path: 'modify_survey', component: ModifySurveyComponent
      },{ 
        path: 'admin_initial_page', component: AdminInitialPageComponent
      }
    ]
  },{ 
    path: 'login_page', component: LoginComponent 
  },{ 
    path: 'user_initial_page', component: UserInitialPageComponent
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
