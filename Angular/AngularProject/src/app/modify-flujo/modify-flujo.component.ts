import { Component } from '@angular/core';

@Component({
  selector: 'app-modify-flujo',
  templateUrl: './modify-flujo.component.html',
  styleUrl: './modify-flujo.component.css'
})
export class ModifyFlujoComponent {
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
