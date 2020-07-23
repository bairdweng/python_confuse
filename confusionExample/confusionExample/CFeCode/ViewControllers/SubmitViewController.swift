//
//  SubmitViewController.swift
//  confusionExample
//
//  Created by bairdweng on 2020/5/25.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class SubmitViewController: UIViewController {

    @IBOutlet weak var hx_btn2: UIButton!
    @IBOutlet weak var hx_Btn1: UIButton!
    @IBOutlet weak var hx_label2: UILabel!
    @IBOutlet weak var hx_textField: UITextField!
    @IBOutlet weak var hx_label1: UILabel!
    @IBOutlet weak var hx_textField2: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        

        // Do any additional setup after loading the view.
    }

    @IBAction func hx_clickOntheBtn1(_ sender: Any) {
        let hx_vc1 = ViewController2()
        self.present(hx_vc1, animated: true, completion: nil)
    }
    
    @IBAction func hx_clickOntheBtn2(_ sender: Any) {
        let hx_vc2 = OneViewController()
        hx_vc2.present(hx_vc2, animated: true, completion: nil)
        
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
