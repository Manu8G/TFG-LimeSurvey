import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CreateSurveyComponent } from './create-survey/create-survey.component'
import { CreateSectionComponent } from './create-section/create-section.component'
import { CreateQuestionComponent } from './create-question/create-question.component';
import { InitialPageComponent } from './initial-page/initial-page.component';

const routes: Routes = [
  { path: 'create_survey', component: CreateSurveyComponent },
  { path: 'create_section', component: CreateSectionComponent },
  { path: 'create_question', component: CreateQuestionComponent },
  { path: 'initial_page', component: InitialPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
