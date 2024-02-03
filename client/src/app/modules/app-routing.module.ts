import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from '@app/pages/main-page/main-page.component';
import { SearchPageComponent } from '@app/pages/search-page/search-page.component';

const routes: Routes = [
    { path: '', redirectTo: '/acceuil', pathMatch: 'full' },
    { path: 'login', component: MainPageComponent },
    { path: 'acceuil', component: SearchPageComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes, { useHash: true })],
    exports: [RouterModule],
})
export class AppRoutingModule {}
