import { Component } from '@angular/core';
import { FillItems } from '@app/classes/researcher-profil';

@Component({
  selector: 'app-vendre',
  templateUrl: './vendre.component.html',
  styleUrls: ['./vendre.component.scss']
})
export class VendreComponent {
  profiles = FillItems();

}
