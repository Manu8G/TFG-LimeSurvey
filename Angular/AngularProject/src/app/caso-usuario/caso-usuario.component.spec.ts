import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CasoUsuarioComponent } from './caso-usuario.component';

describe('CasoUsuarioComponent', () => {
  let component: CasoUsuarioComponent;
  let fixture: ComponentFixture<CasoUsuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CasoUsuarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CasoUsuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
