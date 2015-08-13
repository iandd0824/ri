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
import CryptoSwift



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
        
        
        if ( username.isEqualToString("") || password.isEqualToString("") ) {
            
            var alertView:UIAlertView = UIAlertView()
            alertView.title = "Sign in Failed!"
            alertView.message = "Please enter Username and Password"
            alertView.delegate = self
            alertView.addButtonWithTitle("OK")
            alertView.show()
            
        }
        else {
            
            //let keyString = "Hello this is key"
            //var key2 = [UInt8](keyString.utf8)
            
            //println(key2)
            
            //let ivString = "this is iv"
            //var iv2 = [UInt8](ivString.utf8)
            
            //println(iv2)
            
            //let key: [UInt8] = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
            //let iv: [UInt8] = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F]
            
            let key = "Hello there key!".dataUsingEncoding(NSUTF8StringEncoding)!.arrayOfBytes()
            
            
            
            let iv = Cipher.randomIV(key.count)
            
            let ivstr = NSString(bytes: iv, length: iv.count, encoding: NSUTF8StringEncoding)
            
            
            
            
            let ivString = NSString(bytes: key, length: key.count, encoding: NSUTF8StringEncoding)
            
            let res = NSData(bytes: iv, length: iv.count)

            let resstr = res.base64EncodedStringWithOptions(nil)
            
            println(resstr)

            
            println("ivString")
            println(ivstr)
            
            println("iv:")
            println(iv)
            
            println(key)
            
            let message = "Hello there!".dataUsingEncoding(NSUTF8StringEncoding)!.arrayOfBytes()
            
            let encryptedBytes = ChaCha20(key: key, iv: iv)!.encrypt(message)
            println(encryptedBytes)
            let decryptedBytes = ChaCha20(key: key, iv: iv)!.decrypt(encryptedBytes!)
            let data = NSData.withBytes(decryptedBytes!)
            let decrypted = NSString(bytes: decryptedBytes!, length: decryptedBytes!.count, encoding: NSUTF8StringEncoding)
            
            print(decrypted) // this should print "Hello there!", but it doesn't
        
            
            /*let str = "Hello"
            var buf = [UInt8](str.utf8)

            let utf8 : [UInt8] = [0xE2, 0x82, 0xAC, 0]
            let str2 = NSString(bytes: buf, length: buf.count, encoding: NSUTF8StringEncoding)
            println(str2) // Output: €
            //var buf = [UInt8](str.utf8)
            println(utf8)
            println(buf)
            
            
            let message = [UInt8](count: (count("password") / 2), repeatedValue: 0)
            

            
            
            let key:[UInt8] = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c];
            //let iv:[UInt8] = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F]
            let iv = Cipher.randomIV(AES.blockSize)

            
            let plaintext:[UInt8] = [0x6b,0xc1,0xbe,0xe2,0x2e,0x40,0x9f,0x96,0xe9,0x3d,0x7e,0x11,0x73,0x93,0x17,0x2a]
            let expected:[UInt8] = [0x76,0x49,0xab,0xac,0x81,0x19,0xb2,0x46,0xce,0xe9,0x8e,0x9b,0x12,0xe9,0x19,0x7d];
            
            let str3 = NSString(bytes: plaintext, length: plaintext.count, encoding: NSUTF8StringEncoding)
            
            println("str3")
            println(str3)*/
            
            //let str = "Hello"
            //var buf = [UInt8](str.utf8)
            
            //println(buf);
            //println(encode(buf));
            
            //if let str : String = NSString(data: plaintext, encoding: NSUTF8StringEncoding) {
            //    println(str)
            //} else {
            //    println("not a valid UTF-8 sequence")
           // }
            
            //println(plaintext)
            
            /*if let chacha = ChaCha20(key: key, iv: iv) {
                let encrypted = chacha.encrypt(utf8)
                println(encrypted)
                let data = NSData.withBytes(encrypted!)
                let decrypted = chacha.decrypt(encrypted!)
                println(decrypted)
            }*/
            
            
            /*if let aes = AES(key: key, iv:iv, blockMode: .CBC) {
                //XCTAssertTrue(aes.blockMode == .CBC, "Invalid block mode")
                let encrypted = aes.encrypt(buf, padding: nil)
                println(encrypted)
                //XCTAssertEqual(encrypted!, expected, "encryption failed")
                let decrypted = aes.decrypt(encrypted!, padding: nil)
                println(decrypted)
                //XCTAssertEqual(decrypted!, plaintext, "decryption failed")
            } else {
                //XCTAssert(false, "failed")
            }*/
            
            
            
            
            
            if(username.isEqualToString("admin") && password.isEqualToString("admin")) {
                var prefs:NSUserDefaults = NSUserDefaults.standardUserDefaults()
                prefs.setObject(username, forKey: "USERNAME")
                prefs.setInteger(1, forKey: "ISLOGGEDIN")
                prefs.synchronize()

                self.dismissViewControllerAnimated(true, completion: nil)
            }
            
            /*if let parseJSON = json {
                // Okay, the parsedJSON is here, let's get the value for 'success' out of it
                var success = parseJSON["success"] as? Int
                println("Succes: \(success)")
                
                if(success == 1)
                {
                    NSLog("Login SUCCESS");
                    
                    var prefs:NSUserDefaults = NSUserDefaults.standardUserDefaults()
                    prefs.setObject(username, forKey: "USERNAME")
                    prefs.setInteger(1, forKey: "ISLOGGEDIN")
                    prefs.synchronize()
                    
                    self.dismissViewControllerAnimated(true, completion: nil)
                }
                else {
                    var error_msg:NSString
                    
                    if parseJSON["error_message"] as? NSString != nil {
                        error_msg = parseJSON["error_message"] as! NSString
                    } else {
                        error_msg = "Unknown Error"
                    }
                    var alertView:UIAlertView = UIAlertView()
                    alertView.title = "Sign in Failed!"
                    alertView.message = error_msg as String
                    alertView.delegate = self
                    alertView.addButtonWithTitle("OK")
                    alertView.show()
                }
            }
            else {
                // Woa, okay the json object was nil, something went worng. Maybe the server isn't running?
                let jsonStr = NSString(data: data, encoding: NSUTF8StringEncoding)
                println("Error could not parse JSON: \(jsonStr)")
            }
            
            let user2 = "admin"
            let password2 = "admin"
            
            let plainString = "\(username):\(password)" as NSString
            let plainData = plainString.dataUsingEncoding(NSUTF8StringEncoding)
            let base64String = plainData?.base64EncodedStringWithOptions(NSDataBase64EncodingOptions(rawValue: 0))
            
            Alamofire.Manager.sharedInstance.session.configuration.HTTPAdditionalHeaders = ["Authorization": "Basic " + base64String!]
            
            Alamofire.request(.GET, "http://127.0.0.1:8000/snippets/?format=json")
                .response {(request, response, _, error) in println(response)}
                .responseJSON { (request, response, JSON, error) in println(JSON)}*/
            
        }
        
        
        
    }
    
    class func base64ToByteArray(base64String: String) -> [UInt8]? {
        if let nsdata = NSData(base64EncodedString: base64String, options: nil) {
            var bytes = [UInt8](count: nsdata.length, repeatedValue: 0)
            nsdata.getBytes(&bytes, length: bytes.count)
            return bytes
        }
        return nil // Invalid input
    }

    
     static func encode(bytes: Array<UInt8>) -> String {
        var encodedString = ""
        var decoder = UTF8()
        var generator = bytes.generate()
        var finished: Bool = false
        do {
            let decodingResult = decoder.decode(&generator)
            switch decodingResult {
            case .Result(let char):
                encodedString.append(char)
            case .EmptyInput:
                finished = true
                /* ignore errors and unexpected values */
            case .Error:
                finished = true
            default:
                finished = true
            }
        } while (!finished)
        return encodedString
    }
    
}
