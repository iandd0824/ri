//
//  LoginViewController.swift
//  ri
//
//  Created by Djanny on 8/8/15.
//  Copyright (c) 2015 ptsd.ucla. All rights reserved.
//

import Foundation
import UIKit


class LoginViewController: UIViewController,UITextFieldDelegate {
    
    @IBOutlet var txtUsername : UITextField!
    @IBOutlet var txtPassword : UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}
