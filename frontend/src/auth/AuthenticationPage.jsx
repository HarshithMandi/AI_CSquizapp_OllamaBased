import "react";
import { SignIn,  SignUp, SignedIn, SignedOut} from "@clerk/clerk-react";


export function AuthenticationPage() {
    return <div className="auth-container">
        <SignedIn>
            <div className="redirect-message">
                <h2>You are already signed in.</h2>
            </div>
        </SignedIn>
        <SignedOut>
            <SignIn path="/sign-in" routing="path" signUpUrl="/sign-up" />
            <SignUp path="/sign-up" routing="path" signInUrl="/sign-in" />
        </SignedOut>
    </div>
}