import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AsignarFlujoComponent } from './asignar-flujo.component';

describe('AsignarFlujoComponent', () => {
  let component: AsignarFlujoComponent;
  let fixture: ComponentFixture<AsignarFlujoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AsignarFlujoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AsignarFlujoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
