//
//  LoginViewController.swift
//  ri
//
//  Created by Djanny on 8/8/15.
//  Copyright (c) 2015 ptsd.ucla. All rights reserved.
//

import Foundation
import UIKit

import Alamofire



class LoginViewController: UIViewController,UITextFieldDelegate {
    

    @IBOutlet var txtUsername: UITextField!
    @IBOutlet var txtPassword: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func signinTapped(sender: AnyObject) {
        
        var username:NSString = txtUsername.text
        var password:NSString = txtPassword.text
        
        let user2 = "admin"
        let password2 = "admin"
        
        let plainString = "\(username):\(password)" as NSString
        let plainData = plainString.dataUsingEncoding(NSUTF8StringEncoding)
        let base64String = plainData?.base64EncodedStringWithOptions(NSDataBase64EncodingOptions(rawValue: 0))
        
        Alamofire.Manager.sharedInstance.session.configuration.HTTPAdditionalHeaders = ["Authorization": "Basic " + base64String!]
        
        Alamofire.request(.GET, "http://127.0.0.1:8000/snippets/?format=json")
            .response {(request, response, _, error) in
                println(response)}
            .responseJSON { (request, response, JSON, error) in
                println(JSON)}
        
    }
    
}
