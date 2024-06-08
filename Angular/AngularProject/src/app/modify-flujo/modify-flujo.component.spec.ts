import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModifyFlujoComponent } from './modify-flujo.component';

describe('ModifyFlujoComponent', () => {
  let component: ModifyFlujoComponent;
  let fixture: ComponentFixture<ModifyFlujoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ModifyFlujoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModifyFlujoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
