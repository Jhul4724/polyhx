import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddModifyPageComponent } from './add-modify-page.component';

describe('AddModifyPageComponent', () => {
  let component: AddModifyPageComponent;
  let fixture: ComponentFixture<AddModifyPageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddModifyPageComponent]
    });
    fixture = TestBed.createComponent(AddModifyPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
