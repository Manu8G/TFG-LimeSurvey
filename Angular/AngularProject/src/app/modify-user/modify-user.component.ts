import { Component } from '@angular/core';

@Component({
  selector: 'app-modify-user',
  templateUrl: './modify-user.component.html',
  styleUrl: './modify-user.component.css'
})
export class ModifyUserComponent {
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
