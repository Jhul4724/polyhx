import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from '@app/pages/main-page/main-page.component';
import { SearchPageComponent } from '@app/pages/search-page/search-page.component';

const routes: Routes = [
    { path: '', redirectTo: '/sell', pathMatch: 'full' },
    { path: 'accueil', component: MainPageComponent },
    { path: 'vendre', component: SearchPageComponent },
    { path: 'inscrire', component: SearchPageComponent },
    { path: 'connecter', component: SearchPageComponent },
    { path: 'acheter', component: SearchPageComponent },

];

@NgModule({
    imports: [RouterModule.forRoot(routes, { useHash: true })],
    exports: [RouterModule],
})
export class AppRoutingModule {}
