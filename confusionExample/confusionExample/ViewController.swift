//
//  ViewController.swift
//  confusionExample
//
//  Created by bairdweng on 2020/4/22.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    func temple() {
        
        let hx_1 = "str1"
        var hx_str:String!
        switch hx_1 {
        case "str1":
            hx_str = "str1"
        case "str2":
            hx_str = "str2"
        case "str3":
            hx_str = "str2"
        case "str4":
            hx_str = "str2"
        case "str5":
            hx_str = "str2"
        case "str6":
            hx_str = "str2"
        default:
            hx_str = "str1"
            break
        }
        _ = NSArray(array: [hx_str!])
        
        if hx_str == "str1" {
            let hx_att = [hx_str]
            _ = hx_att
        }
        else {
            let hx_att2 = [hx_str,hx_str,hx_str]
            _ = hx_att2
        } 
    }
}
