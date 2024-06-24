import { Component } from '@angular/core';
import { FlujoService } from '../services/flujo/flujo.service'

@Component({
  selector: 'app-modify-flujo',
  templateUrl: './modify-flujo.component.html',
  styleUrl: './modify-flujo.component.css'
})
export class ModifyFlujoComponent {
  items: any[] = [];

  constructor(private flujoService: FlujoService) {}

  ngOnInit(): void {
    this.flujoService.listFlujos().subscribe({
      next: (response) => {
        let keys = Object.keys(response);
        let values = Object.values(response);
        
        for(let i = 0; i < keys.length; i++){
          this.items.push(values[i]);
        }
      },
      error: (err) => {
        console.error('Error:', err);
      }
    });
  }

  deleteItem(): void {
  }

  updateItem(): void {
    
    
  }
}
