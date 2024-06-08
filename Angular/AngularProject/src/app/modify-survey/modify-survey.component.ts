import { Component } from '@angular/core';

@Component({
  selector: 'app-modify-survey',
  templateUrl: './modify-survey.component.html',
  styleUrl: './modify-survey.component.css'
})
export class ModifySurveyComponent {
  items: string[] = [];

  constructor() {}

  ngOnInit(): void {
    this.items = ['USU1','USU2','USU3','USU4','USU5','USU6','USU7'];
  }

  deleteItem(): void {
      // Refresh the list
  }

  updateItem(): void {
    
    
  }
}
