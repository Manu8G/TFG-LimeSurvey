import { Component } from '@angular/core';

@Component({
  selector: 'app-pruebas',
  templateUrl: './pruebas.component.html',
  styleUrl: './pruebas.component.css'
})
export class PruebasComponent {
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
