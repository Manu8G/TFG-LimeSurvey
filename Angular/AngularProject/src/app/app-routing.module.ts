import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CreateSurveyComponent } from './create-survey/create-survey.component'
import { CreateSectionComponent } from './create-section/create-section.component'
import { CreateQuestionComponent } from './create-question/create-question.component';
import { LoginComponent } from './login/login.component';
import { LayoutComponent } from './layout/layout.component';
import { AuthGuard } from './guards/auth.guard';
import { CreateFlujoComponent } from './create-flujo/create-flujo.component';

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
      }
    ]
  },
  { path: 'login_page', component: LoginComponent },
  //{ path: 'create_survey', component: CreateSurveyComponent },
  //{ path: 'create_section', component: CreateSectionComponent },
  //{ path: 'create_question', component: CreateQuestionComponent },
  //{ path: 'initial_page', component: InitialPageComponent },
  //{ path: 'login_page', component: LoginComponent },
  //{ path: '', redirectTo: '/login_page', pathMatch: 'full' }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
