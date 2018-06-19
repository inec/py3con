using System;
using Microsoft.AspNetCore.Http;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using myWebAppp.Models;

namespace myWebAppp.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("home")]
        public IActionResult Index(string paymentId)
        {
            paymentId+= "-s-"+Request.Headers["Referer"].ToString()+"-e-"; //Microsoft.AspNetCore.Http.HttpRequest.Request.Headers["Referer"];
             ViewData["Message"] = "nameliindex iptione."+paymentId;
               
            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "about application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
