import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { PrivacyPolicyComponent } from './components/privacy-policy/privacy-policy.component';
import { TermsAndConditionsComponent } from './components/terms-and-conditions/terms-and-conditions.component';


const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'privacy-policy', component: PrivacyPolicyComponent},
  {path: 'terms-and-conditions', component: TermsAndConditionsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
