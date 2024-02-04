import { Component } from '@angular/core';
import { FillItems } from '@app/classes/researcher-profil';

@Component({
    selector: 'app-researchers-list',
    templateUrl: './sell.component.html',
    styleUrls: ['./sell.component.scss'],
})
export class ResearchersListComponent {
    profiles = FillItems();
}
