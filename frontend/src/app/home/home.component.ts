import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { User } from '../_models';
import { AuthenticationService } from '../_services';
import { environment } from '../../environments/environment';
import { first } from 'rxjs/operators';

@Component({ templateUrl: 'home.component.html' })
export class HomeComponent implements OnInit {
    currentUser: User;
    userForm: FormGroup;
    update = false;
    backend_url = environment.backend

    constructor(
        private authenticationService: AuthenticationService,
        private formBuilder: FormBuilder,
        private router: Router,
    ) {
        this.currentUser = this.authenticationService.currentUserValue;
    }

    get f() { return this.userForm.controls; }

    ngOnInit() {
        this.userForm = this.formBuilder.group({
            avatar: [''],
            first_name: [''],
            last_name: [''],
            username: [''],
            email: [''],
            password: ['']
        });
        this.userForm.patchValue({
            first_name: this.currentUser.first_name,
            last_name: this.currentUser.last_name,
            username: this.currentUser.username,
            email: this.currentUser.email,
          });
    }

    updateButton(status: boolean) {
        this.update = status;
    }
    onSubmit() {
        this.authenticationService.editUser(this.userForm.value)
        .pipe(first())
        .subscribe(
            data => {
                window.location.reload();
            },
            error => {
                alert(error.message)
            });
    }
    upload(event) {
        const file = (event.target as HTMLInputElement).files[0];
        this.userForm.patchValue({
          avatar: file
        });
        this.userForm.get('avatar').updateValueAndValidity()
     }
}